{
  # To understand Flakes syntax, please see [1]
  # [1] - https://nixos.wiki/wiki/Flakes

  description = "Selenium python bot.";

  inputs = {
    nixpkgs = {
      url = "github:NixOS/nixpkgs";
    };

    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };

  outputs = { self, nixpkgs, flake-utils }:
    let pname = "abbot";
        version = 0.1;
        # Just aliasing things.
    in
      flake-utils.lib.eachDefaultSystem (system:
          let
            pkgs = nixpkgs.legacyPackages.${system};
            python = pkgs.python38;
            pythonPkgs = python.pkgs;

            # # The application itself.
            # abbot = import ./default.nix { inherit pkgs python; };
            # Build an executable Python application
            abbot = pythonPkgs.buildPythonApplication {
              inherit pname version;

              # Our source code is located right here.
              src = ./.;

              # 'propagatedBuildInputs' is a fancy way of saying
              # "Hey Nix, please make sure these dependencies are available after we build the application." 
              propagatedBuildInputs = [
                  # Web drivers
                  pkgs.chromedriver

                  # Python dependencies
                  pythonPkgs.certifi
                  pythonPkgs.dnspython
                  pythonPkgs.idna
                  pythonPkgs.requests
                  pythonPkgs.requests-toolbelt
                  pythonPkgs.urllib3
              ];
            };
            # This Shell env is helpful for just playing around with new approaches.
            # It contains a new shell that has all the dependencies you'd expect. 
            # Feel free to have fun and experiment!
            # 
            # Run `nix develop` from this directory to enter the shell.
            shellEnv = pkgs.mkShell {
              # shellHook = ''
              #   # Patch Visual Studio Code's `packages.json` so that nix's *python* is used as default value for `python.pythonPath`.
              #   if [ -e "./.vscode/settings.json" ]; then
              #     substituteInPlace ./.vscode/settings.json \
              #       --replace \"python.defaultInterpreterPath\"  \"${python}/bin/python\"
              #   fi
              #   printf "\nSet VSCode's python to: ${python}/bin/python \n"
              # '';

              buildInputs = [
                pkgs.bash
                pkgs.bashInteractive
                pkgs.locale
                pkgs.xtermcontrol
                pkgs.xterm
                pkgs.zsh

                pkgs.jq
              ];

              propagatedBuildInputs = abbot.propagatedBuildInputs ++
              [
                # A fun, easy-to-use python REPL for easy debugging and trying 
                # new ideas :)
                pythonPkgs.bpython
              ];
            };

            docker = pkgs.dockerTools.buildImage {
                name = pname;
                tag = "latest";

                created = "now";
                config = {
                  Cmd = [ ];
                  # Runs 'poretitioner' by default.
                  Entrypoint = [ "${abbot.outPath}/bin/${abbot.pname}" ];
                };
              }; 

          in {            
              packages.${pname} = abbot;
              defaultApp = abbot;

              defaultPackage = self.packages.${system}.${pname};

              devShell = shellEnv;

              # dockero = {}: pkgs.dockerTools.buildImage {
              #   name = pname;
              #   tag = "latest";

              #   created = "now";
              #   config = {
              #     Cmd = [ ];
              #     # Runs 'poretitioner' by default.
              #     Entrypoint = [ "${abbot.outPath}/bin/${abbot.pname}" ];
              #   };
              # }; 
          }
      );
}

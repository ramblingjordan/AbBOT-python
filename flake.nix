{
  # To understand Flakes syntax, please see [1]
  # [1] - https://nixos.wiki/wiki/Flakes

  description = "A tool for concerned citizens to report licentious activities of a scandalous nature.";

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
        version = "0.1";
    in
      flake-utils.lib.eachDefaultSystem (system:
          let
            pkgs = nixpkgs.legacyPackages.${system};
            python = pkgs.python39;
            pythonPkgs = python.pkgs;

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

            # Build an executable Python application
            abbot = pythonPkgs.buildPythonApplication {
              inherit pname version;

              # Our source code is located right here.
              src = ./.;

              inherit propagatedBuildInputs;
            };

            # This Shell env is helpful for just playing around with new approaches.
            # It contains a new shell that has all the dependencies you'd expect. 
            # Feel free to have fun and experiment!
            # 
            # Run `nix develop` from this directory to enter the shell.
            shellEnv = pkgs.mkShell {
              shellHook = ''
                # Patch Visual Studio Code's workspace `settings.json` so that nix's python is used as default value for `python.pythonPath`.
                # That way, the debugger will know where all your dependencies are, etc.
                #
                if [ -e "./.vscode/settings.json" ]; then
                  echo "Setting VSCode Workspace's Python path for Nix:"
                  cat .vscode/settings.json  | jq '. + {"python.pythonPath": "${python}/bin/python"}' | tee .vscode/settings.json | grep "python.pythonPath"
                fi
              '';

              buildInputs = [
                pkgs.bash
                pkgs.bashInteractive
                pkgs.locale
                pkgs.xtermcontrol
                pkgs.xterm
                pkgs.zsh
                pkgs.jq

                python
              ] ++ propagatedBuildInputs;
            };

          in {            
              packages.${pname} = abbot;
              defaultApp = abbot;

              defaultPackage = self.packages.${system}.${pname};

              devShell = shellEnv;
          }
      );
}

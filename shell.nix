with import <nixpkgs> {};
  mkShell {
    packages = [
      pyright

      (python3.withPackages (
        packages:
          with packages; [
            black # needs to be here for jupyterlab to work

            matplotlib
            pygame
            requests
            pandas
            pillow

            # python3 -m jupyterlab
            jupyterlab
            ipykernel
          ]
      ))

      plantuml
    ];
  }

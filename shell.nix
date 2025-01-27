with import <nixpkgs> {};
  mkShell {
    packages = [
      black
      pyright

      (python312.withPackages (
        packages:
          with packages; [
            matplotlib
            pygame
            requests
            pandas
          ]
      ))

      plantuml
    ];
  }

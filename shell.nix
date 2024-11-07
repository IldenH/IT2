with import <nixpkgs> {};
  mkShell {
    packages = [
      black
      pyright

      python312Packages.matplotlib
      python312Packages.pygame

      plantuml
    ];
  }

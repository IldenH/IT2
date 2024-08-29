with import <nixpkgs> {};
  mkShell {
    packages = [
      black
      pyright

      python312Packages.matplotlib
    ];
  }

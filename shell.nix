with import <nixpkgs> {};
  mkShell {
    packages = [
      black
      pyright

      python311Packages.matplotlib
    ];
  }

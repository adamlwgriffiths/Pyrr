let
  pypiDataRev="7f28322aa7baec80e261002076e7b322f153e12f";
  pypiDataSha256="1dj7dg4j0qn9a47aw9fqq4wy9as9f86xbms90mpyyqs0i8g1awjz"; ## commit: master # 2021-08-29T07:53:42Z # DavHau/pypi-deps-db
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix/";
    ref = "3.3.0";
  }) {
    inherit pypiDataRev pypiDataSha256;
  };
  pkgs =  mach-nix.nixpkgs;
  custom-python = mach-nix.mkPython {
    python = "python38";
    requirements = ''
      numpy
      multipledispatch
      pytest
      sphinx
    '';
  };
in pkgs.mkShell {
  buildInputs = with pkgs; [
    custom-python
    # sphinx
    gnumake
  ];
}

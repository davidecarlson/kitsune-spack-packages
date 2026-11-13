from spack.package import *
from spack_repo.builtin.build_systems.r import RPackage

class RAssorthead(RPackage):
    """Assorted Header-Only C++ Libraries."""

    homepage = "https://bioconductor.org/packages/assorthead"
    bioc = "assorthead"

    version(
        "1.6.4",
        url="https://bioconductor.org/packages/3.23/bioc/src/contrib/assorthead_1.6.4.tar.gz",
        sha256="a0ef3e48a205c6e70294dda8c113eda0e349db546946a5581c71e84b0d67444d"
    )

    depends_on("r@4.6:", type=("build", "run"))

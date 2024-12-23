import pytest
from mm_eth.anvil import Anvil
from mm_std import Err


@pytest.fixture()
def mnemonic() -> str:
    return "diet render mix evil relax apology hazard bamboo desert sign fence usage baby athlete cannon season busy ten jaguar silk rebel identify foster shrimp"  # noqa


@pytest.fixture()
def anvil(mnemonic):
    res = Anvil.launch(mnemonic=mnemonic)
    if isinstance(res, Err):
        raise Exception(f"can't start anvil: {res.err}")
    a = res.ok
    try:
        yield a
    finally:
        a.stop()


@pytest.fixture
def address_0():
    return "0x10fd602Bff689e64D4720D1DCCCD3494f1f16623"


@pytest.fixture
def private_0():
    return "0x7bb5b9c0ba991275f84b796b4d25fd3a8d7320911f50fade85410e7a2b000632"


@pytest.fixture
def address_1():
    return "0x58487485c3858109f5A37e42546FE87473f79a4b"


@pytest.fixture
def private_1():
    return "0xe4d16faffffa9b28adf02fb5f06998d174046c369d2daffe9a750fbe6a333417"


@pytest.fixture
def address_2():
    return "0x97C77B548aE0d4925F5C201220fC6d8996424309"


@pytest.fixture
def private_2():
    return "0xb7e0b671e176b04ceb0897a698d34771bfe9acf29273dc52a141be6e97145a00"

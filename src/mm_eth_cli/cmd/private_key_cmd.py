from mm_eth import account
from mm_std import fatal, print_plain


def run(private_key: str) -> None:
    try:
        print_plain(account.private_to_address(private_key))
    except Exception as e:
        fatal(f"wrong private key: {e}")

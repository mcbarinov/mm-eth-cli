import json

from mm_eth.solc import solc
from mm_std import Err, PrintFormat, fatal, print_json, print_plain
from mm_std.fs import get_filename_without_extension


def run(contract_path: str, tmp_dir: str, print_format: PrintFormat) -> None:
    contract_name = get_filename_without_extension(contract_path)
    res = solc(contract_name, contract_path, tmp_dir)
    if isinstance(res, Err):
        fatal(res.err)

    bin_ = res.ok.bin
    abi = res.ok.abi

    if print_format == PrintFormat.JSON:
        print_json({"bin": bin_, "abi": json.loads(abi)})
    else:
        print_plain("bin:")
        print_plain(bin_)
        print_plain("abi:")
        print_plain(abi)

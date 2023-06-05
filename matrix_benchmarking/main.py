#!/usr/bin/env python3

import sys, os
import logging

try:
    import fire
except ModuleNotFoundError:
    logging.error("MatrixBenchmarking requires the Python `fire` package, see requirements.txt for a full list of requirements")
    sys.exit(1)

import matrix_benchmarking.visualize
import matrix_benchmarking.benchmark
import matrix_benchmarking.parse
import matrix_benchmarking.download
import matrix_benchmarking.upload_lts
import matrix_benchmarking.download_lts
import matrix_benchmarking.export_schema

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"),
                    format="%(levelname)s | %(message)s",)

class MatrixBenchmarking:
    """
    Commands for launching MatrixBenchmarking
    """

    def __init__(self):
        self.benchmark = matrix_benchmarking.benchmark.main
        self.visualize = matrix_benchmarking.visualize.main
        self.parse = matrix_benchmarking.parse.main
        self.download = matrix_benchmarking.download.main
        self.upload_lts = matrix_benchmarking.upload_lts.main
        self.download_lts = matrix_benchmarking.download_lts.main
        self.export_schema = matrix_benchmarking.export_schema.main

def main():
    # Print help rather than opening a pager
    fire.core.Display = lambda lines, out: print(*lines, file=out)

    # Launch CLI, get a runnable
    runnable = None
    runnable = fire.Fire(MatrixBenchmarking())

    # Run the actual workload
    if hasattr(runnable, "run"):
        return runnable.run()
    else:
        # CLI didn't resolve completely - either by lack of arguments
        # or use of `--help`. This is okay.
        pass


if __name__ == "__main__":
    sys.exit(main())

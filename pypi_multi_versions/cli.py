# pypi_multi_versions/cli.py
import argparse
from pypi_multi_versions.installer import install_version
from pypi_multi_versions.importer import import_version

def main():
    parser = argparse.ArgumentParser(description="Handle multiple versions of PyPI packages.")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for the 'install' command
    install_parser = subparsers.add_parser('install', help='Install a specific version of a package')
    install_parser.add_argument('--package', type=str, required=True, help='Name of the package to install')
    install_parser.add_argument('--version', type=str, required=True, help='Version of the package to install')
    install_parser.add_argument('--path', type=str, required=True, help='Path to install the package')

    # Subparser for the 'import' command
    import_parser = subparsers.add_parser('import', help='Import a specific version of an installed package')
    import_parser.add_argument('--package', type=str, required=True, help='Name of the package to import')
    import_parser.add_argument('--version', type=str, required=True, help='Version of the package to import')
    import_parser.add_argument('--path', type=str, required=True, help='Path from where to import the package')

    args = parser.parse_args()

    if args.command == 'install':
        install_version(args.package, args.version, args.path)
    elif args.command == 'import':
        # Import functionality might not be practical in CLI
        print("Import functionality is available in the Python interface.")

if __name__ == "__main__":
    main()

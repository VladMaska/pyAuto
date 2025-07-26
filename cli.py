import argparse
from pyauto import renamer, backup, cleaner

def main():
    parser = argparse.ArgumentParser(description="pyAuto - automation tools")
    subparsers = parser.add_subparsers(dest="command")

    rename_parser = subparsers.add_parser("rename")
    rename_parser.add_argument("--folder", required=True)
    rename_parser.add_argument("--pattern", required=True)
    rename_parser.add_argument("--start", type=int, default=1)

    backup_parser = subparsers.add_parser("backup")
    backup_parser.add_argument("--folder", required=True)
    backup_parser.add_argument("--dest", required=True)

    clean_parser = subparsers.add_parser("clean")
    clean_parser.add_argument("--folder", required=True)
    clean_parser.add_argument("--ext", required=True, help="Comma-separated extensions")

    args = parser.parse_args()

    if args.command == "rename":
        renamed = renamer.rename_files(args.folder, args.pattern, args.start)
        print("Renamed files:")
        for f in renamed:
            print(f)
    elif args.command == "backup":
        path = backup.backup_folder(args.folder, args.dest)
        print(f"Backup created at {path}")
    elif args.command == "clean":
        exts = args.ext.split(",")
        deleted = cleaner.clean_folder(args.folder, exts)
        print("Deleted files:")
        for f in deleted:
            print(f)
    else:
        parser.print_help()

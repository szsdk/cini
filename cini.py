import sys
import configparser
import click


@click.command(help='Example: cini "section1.item1=new"  "section2.item2=new" -f cfg.ini')
@click.argument("kv", type=str, nargs=-1)
@click.option("--file", "-f", help="file name")
@click.option("--inplace", "-i", help="inplace", default=False, is_flag=True)
def main(file, kv, inplace):
    config = configparser.ConfigParser()
    config.read(file)
    for k, v in map(lambda x: x.split("="), kv):
        sec, item = k.split(".")
        if sec not in config:
            config.add_section(sec)
        config[sec][item] = v
    if not inplace:
        config.write(sys.stdout)
    else:
        with open(file, "w") as fp:
            config.write(fp)


if __name__ == "__main__":
    main()

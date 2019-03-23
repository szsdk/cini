import sys
import configparser
import click


@click.command()
@click.argument("kv", type=str, nargs=-1)
@click.option("--file", "-f", help="file name")
@click.option("--inplace", "-i", help="inplace", default=False, is_flag=True)
def main(file, kv, inplace):
    config = configparser.ConfigParser()
    config.read(file)
    print(config.sections())
    for k, v in map(lambda x: x.split("="), kv):
        sec, item = k.split(".")
        print(sec, item, v)
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

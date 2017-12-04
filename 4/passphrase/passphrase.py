import click


def validation(passphrases):
    valid_passphrases = []
    for passphrase in passphrases:
        words = passphrase.split()

        # Create dictionary of character count for each word
        character_counts = [{c: word.count(c) for c in word} for word in words]

        # Then filter any that have duplicates
        if all(character_counts.count(character_count) == 1 for character_count in character_counts):
            valid_passphrases.append(passphrase)

    return valid_passphrases


@click.command()
@click.option('--passphrases_file', type=click.File())
def cli(passphrases_file):
    passphrases = [passphrase for passphrase in passphrases_file.read().split('\n') if len(passphrase.strip())]
    valid_passphrases = validation(passphrases)
    [print('{} -> {}'.format(passphrase, passphrase in valid_passphrases)) for passphrase in passphrases]
    print('Total {}'.format(len(valid_passphrases)))


if __name__ == '__main__':
    cli()

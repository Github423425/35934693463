import codecs
import sys
import argparse
import logging
from lib.brainwallet import BrainWallet


def main():
    # Script argument parsing
    parser = argparse.ArgumentParser(description='A script to perform bruteforce dictionary attacks on brainwallets.')
    parser.add_argument('-d', action='store', dest='dict_file',
                        help='Dictionary file (e.g. dictionary.txt)', required=True)
    parser.add_argument('-o', action='store', dest='output_file',
                        help='Output file (e.g. output.txt)', required=True)
    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-6s line %(lineno)-4s %(message)s')


						
	# Open dictionary file for reading
    logging.info("Opening dictionary file {} for reading".format(args.dict_file))
    try:
        f_dictionary = codecs.open(args.dict_file, 'r', 'utf8', 'ignore')
    except Exception as e:
        logging.error("Failed to open dictionary file {}. Error: {}".format(args.dict_file, e.args))
        sys.exit(1)

    # Open output file for found addresses
    file_header = 'dictionary word, wallet address, private address'
    logging.info("Opening output file {} for writing".format(args.output_file))
    try:
        f_found_addresses = codecs.open(args.output_file, 'w', 'utf8', 'ignore')
        logging.info(file_header)
        f_found_addresses.writelines(file_header + '\n')
    except Exception as e:
        logging.error("Failed to open output file {}. Error: {}".format(args.found_file, e.args))
        sys.exit(1)

    # Loop through dictionary
    for raw_word in f_dictionary:
        dictionary_word = raw_word.rstrip()
        if not dictionary_word:
            continue

        # Create brainwallet
        brain_wallet = BrainWallet(dictionary_word)

        # Output results
        output = '{},{},{}'.format(dictionary_word, brain_wallet.address,
                                                    brain_wallet.private_key)
        logging.info(output)
        f_found_addresses.write(output + '\n')

    # Close files and connection
    f_found_addresses.close()
    f_dictionary.close()

if __name__ == '__main__':
    main()
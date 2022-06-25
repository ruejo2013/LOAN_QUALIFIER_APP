# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.

    Return:
        A csv file of bank list that is willing to give the applicant the loan
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    csvpath = questionary.text("Enter a name for your (.csv) file:").ask()
    csvpath = Path(csvpath)

    if not csvpath:
        sys.exit("That is not a valid file path")
    header = [
        "Lender",
        "Max Loan Amount",
        "Max LTV",
        "Max DTI",
        "Min Credit Score",
        "Interest Rate",
    ]
    with open(csvpath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(header)

        for keys in qualifying_loans:
            writer.writerow(keys)
        


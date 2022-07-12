# Create a csv of dummy NPI numbers

This is a simply Python script that will allow the user to create a `.csv` file of a list of dummy NPIs.

I built this, to save time when creating different spreadsheets for testing purposes.

## How to use

Make sure you have [pipenv](https://pipenv.pypa.io/en/latest/) installed, this is like npm but for Python.

Then clone the repo to a directory of your choosing.

```bash
> git clone https://
```

Once you have cloned the repo, it's time to install its dependencies. Make sure you're in the root of the repo in the terminal. Then run the following command.

```bash
> pipenv install
```

The only depencey we need here is [Pandas](https://pandas.pydata.org)

Once everything has been installed correctly it's now time to generate your dummy list run `python main.py` like below. You will then be prompted for how many npis are required.

```bash
> python main.py             
How many NPI numbers do you want to create? 
```

After entering your chosen number and pressing enter a .`csv` will be downloaded to your Desktop
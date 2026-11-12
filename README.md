# Space Explorer (Week 5)

A small Python app that talks to NASA's free API.
You type a date and it shows photos of Earth taken from space that day,
plus the asteroids that flew past Earth.

## Files

| File | What it does | Your job |
|---|---|---|
| `main.py` | The menu. Runs the app. | Nothing (already done) |
| `config.py` | Loads your API key from `.env` | Level 1 |
| `api.py` | Talks to NASA | Level 2 and 3 |
| `.env.example` | Shows what your `.env` should look like | Copy it |
| `.gitignore` | Keeps `.env` off GitHub | Nothing |
| `requirements.txt` | The packages we need | Install them |

## Setup

1. Open this folder in VS Code (File > Open Folder).
2. Open the terminal (Terminal > New Terminal).
3. Install the packages:

   ```
   pip install -r requirements.txt
   ```

   On Mac, use `pip3` if `pip` does not work.

## Level 1: Get your key working

1. Go to https://api.nasa.gov and fill in the "Generate API Key" form.
   Your key shows up on the page and in your email.
2. In VS Code, make a copy of `.env.example` and name the copy `.env`
3. Paste your key into `.env` so it looks like this (no quotes, no spaces):

   ```
   NASA_API_KEY=abc123yourkeyhere
   ```

4. Open `config.py` and do the two TODOs.
5. Run it:

   ```
   python main.py
   ```

   On Mac, use `python3 main.py` if `python` does not work.
   You should see "Key loaded!"

## Level 2: Earth from space

Open `api.py` and finish `get_earth_photos(date)`. There are three TODOs (A, B, C).
We do this one together on the projector.

Test it: run `main.py`, pick option 1, and type a date like `2026-03-09`.
The camera started in June 2015, so older dates have no photos.
A few newer days are missing too. If you get none, try another date.

## Level 3: Asteroids

Finish `get_asteroids(date)` in `api.py`. It follows the same pattern as Level 2,
so look at your own code from Level 2 when you get stuck.

Test it: run `main.py`, pick option 2, and type any date. Try your birthday.

## Level 4: Bonus (pick one)

- **Save the photo.** Make an `images/` folder first. Then write `save_photo(link)`
  in `api.py` that downloads the Earth photo and saves it in that folder.
  Call it from `show_earth()` in `main.py`.
  Hint: `requests.get(link).content` gives you the image bytes,
  and `open(filename, "wb")` lets you write bytes to a file.
- **Biggest asteroid.** Add a menu option that prints only the biggest asteroid
  for a date. Look at `show_asteroids()` in `main.py` to see how to get the size.

## If something breaks

| What you see | What it means |
|---|---|
| `No key found` | `.env` is missing, named wrong, or `config.py` is not finished |
| `Error: 403` | NASA did not accept your key. Check for typos or extra spaces in `.env` |
| `Error: 400` | Bad date. Use `YYYY-MM-DD`, like `2015-03-09` |
| `Error: 429` | Too many requests. Wait a bit |
| `ModuleNotFoundError` | Run the `pip install` step again |
| `Nothing came back` | The function still returns None. Check that you finished it |

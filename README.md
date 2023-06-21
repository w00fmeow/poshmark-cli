# poshmark cli

```
      ___                  ___
     (o o)                (o o)
    (  V  ) poshmark cli (  V  )
    --m-m------------------m-m--

  Share your listings automatically

```

## Authentication

Poshmark uses captcha for the login process and I will not try to solve it in this project nor add paid dependencies.

1. The solution is to login via regular browser.
2. Copy request headers from network tab to `headers.txt` file that my script will read.
3. When cookie expire redo the the process. ( it should be ok for a month or so )

## Running

1. Install dependencies: `python3 -m pip install -r requirements.pip`

2. Rename `headers.txt.example` to `headers.txt`
3. Open up your browser and login
4. AFTER THAT (!) Copy request headers from browser's network tab to `headers.txt` file
5. Run the the script

**NOTE**: for now, username is required for the script to work.

```
usage: poshmark-cli.py [-h] --username USERNAME

Poshmark CLI

options:
  -h, --help           show this help message and exit
  --username USERNAME  User name
```

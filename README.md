[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

projectElite
============

Setting up a local dev environment.

Install pip:
- Windows: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows
- Mac: `sudo easy_install pip`


```
$ pip install -r requirements.txt
$ python hello.py
 * Running on http://localhost:5000/
```

Now changes to files in the `static` and `templates` folder will show up *immediately* after you save.

However, if you modify the `hello.py` file, you have to stop Python and restart again via `Ctrl+c` and running `python hello.py` again.





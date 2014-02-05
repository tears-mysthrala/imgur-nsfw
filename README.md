# Imgur NSFW

This is a basic Python script which changes your GNOME/Mac/XFCE/Windows wallpaper to a NSFW image from Imgur.com

## Setup

### Step 1

Clone the repository

    git clone git@github.com:tyler-king/imgur-nsfw.git

### Step 2

Register for an API key at Imgur by clicking [here](https://imgur.com/signin?redirect=http://api.imgur.com/oauth2/addclient).

Once you have your key, edit `config.yml` and edit the `key` entry replacing it with your own.

You will also have to change the `environment` entry to your desktop session (ie. mac, gnome, kde, etc).

You may also change the gallery or set the type to time or top.

### Step 3

#### Linux/Unix

Add it to your crontab.

    crontab -e

Add these lines and save:

    */15 * * * * /usr/bin/python {PATH TO THE SCRIPT}/script {PATH TO YOUR CONFIG YAML}

The above will run every 15 minutes changing the wallpaper

#### Windows

The Windows script is thanks to [this PowerShell](http://stackoverflow.com/questions/9440135/powershell-script-from-shortcut-to-change-desktop) script which I've slightly modified.

You must have Python installed. Located [here](http://www.python.org/download/releases/), install for single-user only and 2.7 version is recommended. As well, you must have Python-YAML installed. Located [here](http://pyyaml.org/wiki/PyYAML).

1. Open the `Task Sheduler`
2. On the right sidebar, select `Create Basic Task`
3. For `Name` enter anything you like and click `Next` at the bottom
4. Select `Daily` for the Tigger and click `Next` at the bottom, then `Next` once again
5. For Action, click `Start a Program` and click `Next` at the bottom
6. For `Program/Script` find your Python executable path (in my case it was: *C:\Python27\python*)
7. For `Add Arguments` input the path to the `script` file of this repo (example: *C:\Users\Tyler\Projects\imgur-nsfw\script*)
8. Click `Finish`

The script should now change your desktop daily.

To invoke this command manually (if you wish) open the Command Prompt and run something like: `C:\Python27\python C:\Users\Tyler\Projects\imgur-nsfw\script` and your wallpaper should change.

## Requirments

+ Python
+ Python-YAML

## Tasks

+ Add KDE support
+ Need someone to test XFCE support by setting `xfce` to `environment` in `config.yml`

## Thanks

Thanks to [igorw](http://github.com/igorw) for testing the Mac support.

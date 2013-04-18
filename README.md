# Imgur NSFW

This is a basic Python script which changes your GNOME Shell or Mac wallpaper to a NSFW image from Imgur.com

## Setup

### Step 1

Clone the repository

    git clone git@github.com:tyler-king/imgur-nsfw.git

### Step 2

Register for an API key at Imgur by clicking [here](https://imgur.com/signin?redirect=http://api.imgur.com/oauth2/addclient).

Once you have your key, edit `config.yml` and edit the `key` entry replacing it with your own. You may also change the gallery or set the type to time or top.

### Step 3

Add it to your crontab.

    crontab -e

Add these lines and save:

    */15 * * * * /usr/bin/python {PATH TO THE SCRIPT}/script

The above will run every 15 minutes changing the wallpaper

## Requirments

+ Python
+ Python-YAML

## Tasks

+ Add KDE support
+ Add XFCE support

## Thanks

Thanks to [igorw](http://github.com/igorw) for testing the Mac support.

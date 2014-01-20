News: 
This plugin gets you the news from news.google.co.in(or any other URL, You can change it as you like).

This plugins requires:
    1. feedparser python module.
    2. bitly_api python module.
    3. bitly api account.

- feedparser and bitly_api modules can be installed using "pip". 
- Replace the <username> and <password> (in plugin.py) with your bitly api account credentials. 
- bityl has been used in this plugin to shrink the news URLS.
- clone/copy this News directory to the pulgins directory of your supybot and load it using "@load News" command.
- I mostly use "@" to give a command to my bot. So, I use @News to get the Top Stories from the news.google.co.in.
- There are other commands available in the plugin. @sports - Gets you the sports News, @ent - Entertainment News, @busin - Business News

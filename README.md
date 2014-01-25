journal_metaweblog
==================

A simple MetaWeblog server that allows you to save a relatively clean HTML file locally from Microsoft Word's blog editor or Windows Live Writer.

I use this for keeping a personal journal, which for purposes of technical longevity, I'd like to be saved in fairly vanilla HTML.

The server saves the published posts in your user documents directory, in a subdirectory named "Journal", and an additional subdirectory based on the title of the post. For example, I title my posts with the date in ISO format (2014-01-25), so the saved file would be like this:

~\Documents\Journal\2014\2014-01-25.html

Setting Up Word
---------------

[See this blog posting](http://esmithy.net/2012/06/06/clean-html-from-microsoft-word-rube-goldberg-method/)


Setting Up Windows Live Writer
------------------------------

What blog service do you use?
__Other services__

Add blog account
Web address of your blog:
__http://localhost:8085__
User name:
_Anything_
Password:
_Anything_
Check Remember my password

Select blog type
Type of blog that you are using:
__Metaweblog API__
Remote posting web address for your blog:
__http://localhost:8085__

Select blog
__Save HTML__

Download Blog Theme
__No__


Known Issues
------------

* Doesn't save embedded media files, just text.
* Doesn't handle GET requests to retrieve the post/file.


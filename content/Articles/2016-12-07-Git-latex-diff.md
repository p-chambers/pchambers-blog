Title: Git "diff" for Latex Projects
Slug: git-latexdiff
Date: 2016-07-12 17:16:05
Tags: Git, Latex
Category: blog
Author: Paul Chambers
Lang: 

Got some LaTeX files you're working on? Want to know what specific words you have changed, and all `git diff` throws up are entire paragraphs in green and red (if you write without line-breaks), even if you just added a full stop? Well, friend, you may think, as I did, "Surely there's a tool for this?". It turns out there is, and I found the result useful enough that I wanted to write a blog entry on it...

Hopefully you are reading this as you already have the code of your LaTeX project under version control. Even more hopefully, you are using `git` to do so. If not, do not fear; I provide a [minimal example]({attach}/downloads/2016-12-07-git-latexdiff-test.zip), with an initial commit containing only the [Lorem Ipsum](http://www.lipsum.com/) snippet, and a second commit with some additional text. I also assume you have access to a UNIX terminal.

I'll show the output of a few `diff` methods using the example provided. I wanted something that would keep the directory clean, and not involve me hacking a solution, so I'll focus on those. Let's look at a few...

## The Quick and Dirty Method

The first, and more immediate, solution is a very simple flag addition to `git diff`. Enter **`--color-words`**,

	git diff --color-words HEAD~1

This will `diff` between HEAD and the previous commit of the latex source code, showing the specific words that have changed, highlighted in ascii text. That's it. No additional installation and all the rewards. *Magic*!

Here's the terminal output (after some ascii-to-html conversion via `aha`) for my simple example, where <span style="color:red;">red</span> shows text which has been removed and <span style="color:green;">green</span> shows the added text:


<!-- This file was created with the aha Ansi HTML Adapter. http://ziz.delphigl.com/tool_aha.php -->
>
<div style="white-space: pre-wrap; font-size: 9pt">
<span style="font-weight:bold;">diff --git a/main.tex b/main.tex</span>
<span style="font-weight:bold;">index a878dad..b1c5236 100644</span>
<span style="font-weight:bold;">--- a/main.tex</span>
<span style="font-weight:bold;">+++ b/main.tex</span>
<span style="color:teal;">@@ -2,6 +2,8 @@</span>

>\begin{document}

>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis<span style="color:red;">aute irure dolor</span> in reprehenderit in voluptate velit esse <span style="color:green;">aute irure dolor</span> cillum dolore eu fugiat nulla pariatur. Excepteur sint <span style="color:red;">occaecat</span><span style="color:green;">occaecat,</span> cupidatat non proident, sunt in culpa qui <span style="color:red;">officia</span><span style="color:green;">officia;</span> deserunt mollit anim id est laborum.
>
><span style="color:green;">The snippet of Lorem ipsum, presented above, serves no purpose but to fill space. The words are randomised, altered, and removed from some text a guy wrote a long time ago; it doesn't make sense in Latin, or any other language. I can therefore change the order of words, and it may even make more sense than before!</span>
>
>\end{document}
</div>

As a small `git` refresher, you can also `diff` between specific commits. First, find the identifier of the commit (you can use `git log` to do this) - remember, this only requires the first 4 or 5 characters, as `git` is very good at randomising commit IDs. In my example code, the initial commit has the ID **2888d...**, so we'll use that, however the output is the same as above. This method makes a lot more sense in bigger projects with many more commits:

	git diff --color-words 2888d HEAD 

## The `pdf` Method

Ok, so the previous method still required some extra processing to read, as there is still not line wrapping, and not everybody likes reading long latex code in a terminal. Luckily, there's a nifty `difftool` for this, named [latexdiff](http://www.ctan.org/tex-archive/support/latexdiff). This can be found in the `apt-get` package repositories,

	sudo apt-get install latexdiff

I couldn't get this working as an in-line command, but using the alias provided courtesy of [Gautam Iyer's Wiki](https://wiki.math.cmu.edu/iki/wiki/tips/20140301-git-latexdiff.html), which should be added to your `~/.gitconfig` file,

	[alias]
		ldiff = difftool -y -t latex

	[difftool.latex]
		cmd = latexdiff "$LOCAL" "$REMOTE" 


Then, the process of creating a `diff`ed pdf involves simply,

	git ldiff HEAD~1 main.tex > diff.tex

and then your regular method for compiling a pdf from a `.tex` file, in my example I'll use a simple compilation as there are no frills required,

	latex diff.tex && dvipdf diff.dvi 

Check out [the output]({filename}/downloads/2016-12-07-diff.pdf).

## The `pdf` Method: Multiple Source Files

The above method had some issues for my original problem, as the project was split into multiple source files, with non tex files and images. Again, [Gautam Iyer's Wiki](https://wiki.math.cmu.edu/iki/wiki/tips/20140301-git-latexdiff.html) details a reasonable hack for for doing this, but I found a delightful tool named [git-latexdiff](https://gitlab.com/git-latexdiff/git-latexdiff) as pointed to in [this Stack Exchange Thread](http://tex.stackexchange.com/questions/1325/using-latexdiff-with-git). Essentially, this package extracts the entire repository to `/tmp/`, recursively diffs all latex source files and produces the pdf, with no questions asked.

There is no apt-get package for `git-latexdiff`, so you'll need to first follow their instructions on the website. This involves (in a temporary location),

	git clone https://gitlab.com/git-latexdiff/git-latexdiff.git
	cd git-latexdiff && sudo make install

You may also need to install `ascii-doc`, as the documentation uses the `a2x` package. There is no need to edit the `~/.gitconfig` or post-compilation for this solution, simply use, 

	git latexdiff HEAD~1

and out pops the pdf, as before, regardless of non-tex files or multiple .tex files. Phew!

Of course, kudos goes to [Matthieu Moy](https://gitlab.com/u/moy) for `git-latexdiff`, I am merely spreading the word.

**Note**: `git-latexdiff` seems to use the local Makefile in the repository if one exists, even if a specific build is requested, e.g., with the `--latexmk` flag. So ensure this Makefile is able to compile without errors, or remove it.

Happy diffing!

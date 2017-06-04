# [Strip Whitespace Lines](//packagecontrol.io/packages/Strip%20Whitespace%20Lines)

This plugin is an alternative to the default option `trim_trailing_white_space_on_save` which removes any trailing whitespace when the user saves a file.  
Instead of removing whitespace everywhere, this plugin only removes whitespace where the _whole line_ is entirely consistant of whitespace.

You can enable this through the preferences (or syntax-specific) like so:
```json
{
	"strip_whitespace_lines_on_save": true,
}
```

## Installation

##### Using the package manager

1. Install the [Sublime Text Package Control](//packagecontrol.io/installation) plugin if you haven't already.
2. Open up the command palette (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) and enter `Package Control: Install Package`
3. Search for `Strip Whitespace Lines` and hit <kbd>Enter</kbd> to install.
4. Follow the instructions that appears on the screen.

##### Manual installation with Git

1. Click the `Preferences > Browse Packages` menu.
2. Open up a terminal and execute the following:
    - `git clone https://github.com/p3lim/sublime-strip-whitespace-lines Strip\ Whitespace\ Lines`
3. Restart Sublime Text.

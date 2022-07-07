This program is a simple and convenient CLI tool to recursively delete specific files or folders under a specific path.

Because the program will really change data on your disk, be CAREFUL when you use it, no matter how safe it is designed.

For a glinpse and easy understanding, think it as a smart and convenient version of command 'rm' on UNIX-like OS.
Also, you can set this program as one of your OS commands by a little skill as you like.

===========

#Usage:

#-h or --help
‧ For more detailed usage, give the program exactly one argument '-h' or '--help'.

#--version
‧ For version information, give the program exactly one argument '--version'.

#-d/-f
‧ To delete sub-directories/sub-folders with an exactly identical name which you give the program under your current path, you can pass a short option '-d' additionally.
‧ To delete files with an exactly identical name which you give the program under your current path, you can pass a short option '-f' additionally; by default, the program would execute this option if you do not specify an option to delete.
‧ To delete both files and sub-directories/sub-folders with an exactly identical name which you give the program under your current path, you can pass a short option either '-df' or '-fd' additionally; following traditional usage, short options for this program can be mixed together to work without their order in string.

===========

This program is designed to be relatively safe, so you can delete your target files or folders successfully only with an exactly identical name.
And for safety and security, this program would and should NEVER take a regular expression as its argument/parameter.
Besides, you would NOT correctly delete files or folders which you want to delete with a WRONG option to delete.

This program was available as executables with corresponding SHA-256 hash values for verification across Windows, macOS, and some Linux distros.
If you want to use it on an OS other than above, you can execute it via a Python3 interpreter on that OS, or you can build an executable from the source code yourself.

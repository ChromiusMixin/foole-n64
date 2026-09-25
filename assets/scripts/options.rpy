## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Foole's World")

define config.developer = False
define config.rollback_enabled = False

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False

define build.name = "FoolesWorld"

define config.gl_resize = True

# define config.main_menu_music = "main-menu-theme.ogg"

define config.mouse = { }
define config.mouse['default'] = [ ( "gui/cursor.png", 0, 0) ]
define config.mouse['menu'] = [ ( "gui/cursormenu.png", 0, 0) ]
define config.mouse['imagemap'] = [ ( "gui/cursormenu.png", 0, 0) ]
define config.mouse['button'] = [ ( "gui/cursorbutton.png", 0, 0) ]

## Transitions #################################################################
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = None
define config.exit_transition = None


## Between screens of the game menu.

define config.intra_transition = None


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None

## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.

## Window management ###########################################################
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "show"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = None
define config.window_hide_transition = None


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other

default preferences.text_cps = 60


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 0

## Icon ########################################################################
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
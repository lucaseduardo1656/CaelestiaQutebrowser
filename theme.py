import json
import os
from pathlib import Path

def apply_theme(c):
    """
    Applies the Caelestia theme to Qutebrowser by reading the scheme.json file.
    """
    # Determine the path to the scheme file, respecting XDG_STATE_HOME
    state_home = os.getenv("XDG_STATE_HOME", Path.home() / ".local/state")
    scheme_path = Path(state_home) / "caelestia/scheme.json"

    if not scheme_path.exists():
        # You can set a default fallback theme here if you want
        print(f"Caelestia theme file not found at {scheme_path}")
        return

    with open(scheme_path, "r") as f:
        scheme = json.load(f)

    colours = {name: f"#{value}" for name, value in scheme["colours"].items()}

    # Map Caelestia colours to Qutebrowser's config
    # This is a comprehensive mapping based on the zen(Firefox) theme.
    
    # General UI
    c.colors.webpage.bg = colours["surface"]

    # Tabs
    c.colors.tabs.bar.bg = colours["surfaceContainer"]
    c.colors.tabs.indicator.start = colours["primary"]
    c.colors.tabs.indicator.stop = colours["secondary"]
    c.colors.tabs.indicator.error = colours["error"]
    
    c.colors.tabs.odd.bg = colours["surfaceContainer"]
    c.colors.tabs.odd.fg = colours["onSurfaceVariant"]
    c.colors.tabs.even.bg = colours["surfaceContainer"]
    c.colors.tabs.even.fg = colours["onSurfaceVariant"]

    c.colors.tabs.selected.odd.bg = colours["surface"]
    c.colors.tabs.selected.odd.fg = colours["onSurface"]
    c.colors.tabs.selected.even.bg = colours["surface"]
    c.colors.tabs.selected.even.fg = colours["onSurface"]

    # Status Bar
    c.colors.statusbar.normal.bg = colours["primary"]
    c.colors.statusbar.normal.fg = colours["onPrimary"]
    c.colors.statusbar.command.bg = colours["secondary"]
    c.colors.statusbar.command.fg = colours["onSecondary"]
    c.colors.statusbar.caret.bg = colours["tertiary"]
    c.colors.statusbar.caret.fg = colours["onTertiary"]
    c.colors.statusbar.progress.bg = colours["primary"]
    c.colors.statusbar.url.success.http.fg = colours["green"]
    c.colors.statusbar.url.success.https.fg = colours["green"]
    c.colors.statusbar.url.error.fg = colours["error"]
    c.colors.statusbar.url.warn.fg = colours["yellow"]
    c.colors.statusbar.url.hover.fg = colours["sky"]

    # Completion Widget
    c.colors.completion.category.bg = colours["surfaceContainerHigh"]
    c.colors.completion.category.fg = colours["primary"]
    c.colors.completion.even.bg = colours["surfaceContainer"]
    c.colors.completion.odd.bg = colours["surfaceContainerLow"]
    c.colors.completion.fg = colours["onSurface"]
    c.colors.completion.item.selected.bg = colours["primary"]
    c.colors.completion.item.selected.fg = colours["onPrimary"]
    c.colors.completion.item.selected.border.bottom = colours["primary"]
    c.colors.completion.item.selected.border.top = colours["primary"]
    c.colors.completion.match.fg = colours["peach"]
    c.colors.completion.scrollbar.bg = colours["surfaceContainerHighest"]
    c.colors.completion.scrollbar.fg = colours["secondary"]

    # Downloads
    c.colors.downloads.bar.bg = colours["surfaceContainer"]
    c.colors.downloads.start.bg = colours["blue"]
    c.colors.downloads.start.fg = colours["surface"]
    c.colors.downloads.stop.bg = colours["green"]
    c.colors.downloads.stop.fg = colours["surface"]
    c.colors.downloads.error.fg = colours["error"]

    # Hints
    c.colors.hints.bg = colours["peach"]
    c.hints.border = colours["peach"]
    c.colors.hints.fg = colours["background"]
    c.colors.hints.match.fg = colours["onSurface"]
    c.colors.keyhint.bg = colours["surfaceContainer"]
    c.colors.keyhint.fg = colours["primary"]
    c.colors.keyhint.suffix.fg = colours["onSurfaceVariant"]

    # Messages (Errors, Warnings, Info)
    c.colors.messages.error.bg = colours["errorContainer"]
    c.colors.messages.error.fg = colours["onErrorContainer"]
    c.colors.messages.error.border = colours["error"]
    c.colors.messages.warning.bg = colours["yellow"]
    c.colors.messages.warning.fg = colours["background"]
    c.colors.messages.warning.border = colours["yellow"]
    c.colors.messages.info.bg = colours["surfaceContainerHigh"]
    c.colors.messages.info.fg = colours["onSurface"]
    c.colors.messages.info.border = colours["surfaceContainerHigh"]

    # Prompts
    c.colors.prompts.bg = colours["surfaceContainer"]
    c.colors.prompts.fg = colours["onSurface"]
    c.colors.prompts.border = colours["outline"]
    c.colors.prompts.selected.bg = colours["primary"]
    c.colors.prompts.selected.fg = colours["onPrimary"]

    # Content
    c.colors.webpage.darkmode.algorithm = "lightness-cielab"
    c.colors.webpage.darkmode.contrast = 0.0
    c.colors.webpage.darkmode.policy.images = "never"
    c.colors.webpage.darkmode.policy.page = "smart"
    c.colors.webpage.preferred_color_scheme = scheme["mode"]

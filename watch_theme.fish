#!/usr/bin/env fish

if set -q XDG_STATE_HOME
    set state_dir "$XDG_STATE_HOME/caelestia"
else
    set state_dir "$HOME/.local/state/caelestia"
end

mkdir -p "$state_dir"
echo "Watching for changes in $state_dir..."

inotifywait -q -m -e close_write,moved_to,create "$state_dir" | while read dir events file
    if test "$file" = "scheme.json"
        if pgrep -x qutebrowser > /dev/null
           qutebrowser ":config-source"
            # Throttle to prevent command storms
            sleep 1
        else
            echo "Qutebrowser is not running. Skipping reload."
        end
    end
end

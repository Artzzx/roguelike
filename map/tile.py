from __future__ import annotations

import tcod.context
import tcod.tileset
import tcod.event
import tcod.console
import attrs

@attrs.define
class ExempleState:
    player_x: int # x position of the player
 
    player_y: int # y position of the player

    def on_draw(self, console: tcod.console.Console) -> None:
        console.print(self.player_x, self.player_y, "@")

    def on_event(self, event: tcod.event.Event) -> None:
        match event:
            case tcod.event.Quit():
                raise SystemExit()
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                self.player_x -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                self.player_x += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                self.player_y -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                self.player_y += 1

def main() -> None:
    """Load a tileset and open a window using it."""
    tileset = tcod.tileset.load_tilesheet(
        "C:/Users/Marc/Documents/Code/roguelike/data/Alloy_curses_12x12.png", 16, 16, tcod.tileset.CHARMAP_CP437)
    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80, 50)
    state = ExempleState(player_x=console.width // 2, player_y=console.height // 2)
    with tcod.context.new(tileset=tileset) as context:
        while True:
            console.clear()
            state.on_draw(console)
            context.present(console)
            for event in tcod.event.wait():
                print(event)
                state.on_event(event)

if __name__ == "__main__":
    main()

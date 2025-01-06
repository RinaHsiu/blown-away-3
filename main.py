def on_up_pressed():
    simplified.gravity_jump(mySprite)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        0,
        0)
    projectile.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
    animation.run_image_animation(projectile, assets.animation("""
        splode
    """), 100, False)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    tiles.set_wall_at(tiles.location_in_direction(tiles.location_of_sprite(mySprite),
            CollisionDirection.BOTTOM),
        True)
    tiles.set_tile_at(tiles.location_in_direction(tiles.location_of_sprite(mySprite),
            CollisionDirection.BOTTOM),
        assets.tile("""
            bounce
        """))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    tiles.set_tile_at(location, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        orange bauble
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_wall_at(location2, False)
    tiles.set_tile_at(location2, assets.tile("""
        transparency16
    """))
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        skyblock
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        chest1
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        poison pit
    """),
    on_overlap_tile4)

projectile: Sprite = None
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    background
"""))
tiles.set_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(assets.image("""
    stand
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 0)
mySprite.ay = 500
scene.camera_follow_sprite(mySprite)
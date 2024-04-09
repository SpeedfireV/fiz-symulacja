import pygame


def entering_numbers(event_key):
    if event_key == pygame.K_1:
        return "1"
    elif event_key == pygame.K_2:
        return "2"
    elif event_key == pygame.K_3:
        return "3"
    elif event_key == pygame.K_4:
        return "4"
    elif event_key == pygame.K_5:
        return "5"
    elif event_key == pygame.K_6:
        return "6"
    elif event_key == pygame.K_7:
        return "7"
    elif event_key == pygame.K_8:
        return "8"
    elif event_key == pygame.K_9:
        return "9"
    elif event_key == pygame.K_0:
        return "0"
    elif event_key == pygame.K_MINUS:
        return "-"
    elif event_key == pygame.K_MINUS:
        return "."
    return ""

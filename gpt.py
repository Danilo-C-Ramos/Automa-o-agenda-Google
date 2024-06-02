from playwright.sync_api import sync_playwright

def use_profile():
    with sync_playwright() as p:
        # Substitua este caminho pelo caminho do perfil que você encontrou
        user_data_dir = "C:/Users/danil/AppData/Local/Google/Chrome/User Data/Profile 1"
        
        browser = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            args=["--no-sandbox", "--disable-web-security", "--disable-site-isolation-trials", "--disable-blink-features=AutomationControlled"]
        )
        
        page = browser.new_page()
        
        # Navegue até o Google Agenda
        page.goto("https://calendar.google.com/", timeout=60000)
        
        # Aguarde o seletor "Create" estar visível
        page.wait_for_selector("text=Criar", timeout=60000)
        page.click("text=Criar")
        
        page.wait_for_selector("text=Evento", timeout=90000)
         # Obtenha as dimensões e a posição do botão de evento
        button_event = page.locator('text=Evento')
        button_event_rect = button_event.bounding_box()

        # Calcule as coordenadas do centro do botão de evento
        x = button_event_rect['x'] + button_event_rect['width'] / 2
        y = button_event_rect['y'] + button_event_rect['height'] / 2

        # Clique no centro do botão de evento
        page.mouse.click(x, y)
        # Preencha os detalhes do evento
        #page.fill('input[aria-label="Event title"]', "Meu Evento Automatizado")
        #page.click('div[aria-label="Add date and time"]')
        
        # Adicione mais ações conforme necessário, como definir a data, hora e outros detalhes do evento
        
        # Salve o evento (você precisa ajustar o seletor para o botão de salvar conforme necessário)
        page.click('button[aria-label="Save"]')
        
        browser.close()

if __name__ == "__main__":
    use_profile()

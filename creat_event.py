from playwright.sync_api import sync_playwright

def create_event():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # Reutilize o estado da sessão salvo
        context = browser.new_context(storage_state="auth_state.json")
        page = context.new_page()
        
        # Navegue até o Google Agenda
        page.goto("https://calendar.google.com/")
        
        # Aguarde a página carregar completamente
        page.wait_for_selector("text=Create")
        
        # Clique no botão de criar evento
        page.click("text=Create")
        
        # Preencha os detalhes do evento
        page.fill('input[aria-label="Event title"]', "Meu Evento Automatizado")
        page.click('div[aria-label="Add date and time"]')
        
        # Adicione mais ações conforme necessário, como definir a data, hora e outros detalhes do evento
        
        # Salve o evento (você precisa ajustar o seletor para o botão de salvar conforme necessário)
        page.click('button[aria-label="Save"]')
        
        browser.close()

if __name__ == "__main__":
    create_event()

from playwright.sync_api import sync_playwright

def save_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Navegue até a página de login do Google
        page.goto("https://accounts.google.com/")

        # Adicione um tempo de espera para você fazer login manualmente
        print("Por favor, faça o login na sua conta do Google...")
        page.wait_for_timeout(60000)  # Aguarda 1 minuto para você fazer o login
        
        # Salve o estado da sessão
        context.storage_state(path="auth_state.json")
        
        browser.close()

if __name__ == "__main__":
    save_session()

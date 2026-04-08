import customtkinter as ctk


class AppCripto(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações de Janela
        self.title("CipherSuite Pro v2.0")
        self.geometry("1100x600")

        # Configurar grid principal (1 coluna para menu, 1 para conteúdo)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- BARRA LATERAL (Sidebar) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="CIPHER\nMODULAR",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.lbl_algo = ctk.CTkLabel(self.sidebar_frame, text="Algoritmo:")
        self.lbl_algo.grid(row=1, column=0, padx=20, pady=(20, 0))

        self.combo_algo = ctk.CTkComboBox(self.sidebar_frame,
                                          values=["César", "Monoalfabética", "Playfair", "Hill"],
                                          command=self.atualizar_interface_chave)
        self.combo_algo.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(20, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))

        # --- ÁREA CENTRAL ---
        self.main_content = ctk.CTkFrame(self, fg_color="transparent")
        self.main_content.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")
        self.main_content.grid_columnconfigure(0, weight=1)

        # Campo de Entrada
        self.txt_input = ctk.CTkTextbox(self.main_content, height=150, font=("Inter", 14))
        self.txt_input.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        self.txt_input.insert("0.0", "Digite...")

        # Frame da Chave (Dinâmico)
        self.frame_chave_container = ctk.CTkFrame(self.main_content)
        self.frame_chave_container.grid(row=1, column=0, sticky="ew", pady=10)
        self.frame_chave_container.grid_columnconfigure(0, weight=1)

        # Botão de Ação
        self.btn_action = ctk.CTkButton(self.main_content, text="PROCESSAR TEXTO", height=50,
                                        font=ctk.CTkFont(weight="bold"), fg_color="#1f538d", hover_color="#14375e")
        self.btn_action.grid(row=2, column=0, pady=20, sticky="ew")

        # Campo de Saída
        self.txt_output = ctk.CTkTextbox(self.main_content, height=150, font=("Consolas", 14), fg_color="#2b2b2b")
        self.txt_output.grid(row=3, column=0, sticky="ew")

        # Inicialização
        self.widgets_chave = []
        self.atualizar_interface_chave("César")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def atualizar_interface_chave(self, escolha):
        # Limpa widgets anteriores
        for w in self.widgets_chave:
            w.destroy()
        self.widgets_chave = []

        # Título da seção de chave
        lbl = ctk.CTkLabel(self.frame_chave_container, text=f"Configuração da Chave ({escolha})",
                           font=("Inter", 12, "italic"))
        lbl.grid(row=0, column=0, pady=5)
        self.widgets_chave.append(lbl)

        if escolha == "César":
            entry = ctk.CTkEntry(self.frame_chave_container, placeholder_text="Deslocamento (Ex: 3)", width=300)
            entry.grid(row=1, column=0, pady=10)
            self.widgets_chave.append(entry)

        elif escolha == "Hill":
            # Exemplo de Grid para matriz 2x2
            grid_frame = ctk.CTkFrame(self.frame_chave_container, fg_color="transparent")
            grid_frame.grid(row=1, column=0, pady=10)
            for r in range(2):
                for c in range(2):
                    e = ctk.CTkEntry(grid_frame, width=50, placeholder_text="0")
                    e.grid(row=r, column=c, padx=5, pady=5)
                    self.widgets_chave.append(e)

        else:
            entry = ctk.CTkEntry(self.frame_chave_container, placeholder_text="Insira a chave textual...", width=400)
            entry.grid(row=1, column=0, pady=10)
            self.widgets_chave.append(entry)


if __name__ == "__main__":
    app = AppCripto()
    app.after(0, lambda: app.state('zoomed'))  # Inicia maximizado no Windows
    app.mainloop()
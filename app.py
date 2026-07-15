import streamlit as st
import google.generativeai as genai
import time

# --- SETUP AI ---
API_KEY = st.secrets["azzriel_ai_api_key"]
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="(AI) Azzriel Intelligence v3.0", page_icon="💀")

# Fungsi cari model otomatis agar tidak 404
def get_working_model():
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                return m.name
    except:
        return "gemini-pro"
    return "gemini-pro"

if 'prank_active' not in st.session_state:
    st.session_state.prank_active = False

if not st.session_state.prank_active:
    # --- TAMPILAN AI NORMAL (PENYAMARAN) ---
    st.title("(AI) Azzriel Intelligence v3.0")
    st.write("INOVASI TERBARU DALAM TEKNOLOGI AI. Silakan ajukan pertanyaan apa saja.")

    user_input = st.text_input("Input Query:", placeholder="Tanya di sini...")

    if st.button("Generate Response"):
        if user_input.lower() == "#123":
            st.session_state.prank_active = True
            st.rerun()
        elif user_input:
            with st.spinner("Menghubungkan ke Server Pusat..."):
                try:
                    working_model_name = get_working_model()
                    model = genai.GenerativeModel(working_model_name)
                    response = model.generate_content(user_input)
                    st.write(f"**AI:** {response.text}")
                except Exception as e:
                    st.error("Koneksi sibuk. Ketik '#123' untuk bantuan menghubungi bantuan.")
else:
    # --- TAMPILAN PRANK NIGHTMARE MAX (GALAK) ---
    st.markdown("""
        <style>
        .stApp { background-color: #000000; }
        * { color: #FF0000 !important; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #FF0000; }
        @keyframes shake {
            0% { transform: translate(1px, 1px) rotate(0deg); }
            10% { transform: translate(-1px, -2px) rotate(-1deg); }
            20% { transform: translate(-3px, 0px) rotate(1deg); }
            30% { transform: translate(3px, 2px) rotate(0deg); }
            40% { transform: translate(1px, -1px) rotate(1deg); }
            50% { transform: translate(-1px, 2px) rotate(-1deg); }
        }
        .critical { 
            animation: shake 0.5s infinite; 
            font-weight: bold; 
            font-size: 35px; 
            text-align: center; 
            border: 4px double red; 
            padding: 20px;
            background-color: #1a0000;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="critical">💀 SYSTEM BREACHED BY ZRSTUDIO 💀</p>', unsafe_allow_html=True)
    st.write("### 💢 FATAL ERROR: Unauthorized Access Detected")
    st.write("**Exploit Code:** `VX-DEATH-2886` | **Severity:** `YOUR AN IDIOT`")
    
    bar = st.progress(0)
    status_text = st.empty()
    
    # List pesan menakutkan yang lebih banyak dan agresif
    scary_steps = [
        "👺 Initializing Malicious Payload...",
        "🔱 Cracking Local Security Tokens...",
        "📂 Scrambling User Files (Photos, Videos, DB)...",
        "📡 Tunneling Private Data to Dark-Web Cluster...",
        "💀 Extracting Credentials & Banking Tokens...",
        "📸 Camera/Microphone Access: GRANTED.",
        "☢️ RSA-8192 Military-Grade Encryption Applied...",
        "🧨 Deleting System32 & Recovery Partition...",
        "🌐 Propagating to All Contacts on Social Media...",
        "🚨 HARDWARE OVERHEAT INITIATED...",
        "🔚 PERMANENT DISK WIPE: 99% COMPLETE..."
    ]
    
    # Animasi loading yang disesuaikan
    for i in range(1, 101):
        if i < 20: sleep_time = 0.1
        elif 20 <= i < 50: sleep_time = 0.2  # Sangat lambat pas lagi "Scrambling Files"
        elif 50 <= i < 85: sleep_time = 0.15
        else: sleep_time = 0.03  # Ngebut pas mau selesai biar panik
        
        time.sleep(sleep_time)
        bar.progress(i)
        
        step_index = min((i-1) // 9, len(scary_steps) - 1)
        status_text.markdown(f"**CURRENT THREAT:** `{scary_steps[step_index]}`")
            
    st.error("❗SYSTEM IS UNRECOVERABLE. ❗")
    st.warning("ALL YOUR DATA HAS BEEN STOLEN, YOUR AN IDIOT.")
    
    if st.button("👹 ABORT MISSION (IF YOU CAN)"):
        st.session_state.prank_active = False

        st.rerun()

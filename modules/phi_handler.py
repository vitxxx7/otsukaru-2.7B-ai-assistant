from llama_cpp import Llama
import yaml

class Phi2Model:
    def __init__(self):
        self.config = self._load_config()
        self.llm = self._init_model()
        
    def _load_config(self):
        with open('configs/model_config.yaml') as f:
            return yaml.safe_load(f)
            
    def _init_model(self):
        return Llama(
            model_path=self.config['model_params']['model_path'],
            n_ctx=self.config['model_params']['n_ctx'],
            n_threads=self.config['model_params']['n_threads'],
            n_gpu_layers=self.config['model_params']['n_gpu_layers'],
            verbose=False
        )
        
    def generate(self, prompt):
        return self.llm(
            prompt,
            temperature=self.config['model_params']['temp'],
            top_k=self.config['model_params']['top_k'],
            top_p=self.config['model_params']['top_p'],
            max_tokens=self.config['model_params']['max_tokens'],
            stop=self.config['model_params']['stop']
        )
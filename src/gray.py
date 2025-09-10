---

### 3. Pasta `assets/` com a imagem

- **`assets/lena_color.png`**  
  - Coloque aqui a imagem original colorida de Lena (512×512), para entrada no processo.

---

### 4. `src/gray.py`

```python
"""
gray.py
Converte uma imagem colorida para tons de cinza (0–255).
"""

import sys
from pathlib import Path
import numpy as np
from PIL import Image

def to_grayscale(input_path: Path, output_path: Path):
    img = Image.open(str(input_path)).convert("RGB")
    arr = np.array(img, dtype=np.float32)
    # Fórmula de luminância: weights aproximadas de percepção humana
    gray = (0.299 * arr[..., 0] + 0.587 * arr[..., 1] + 0.114 * arr[..., 2]).astype(np.uint8)
    gray_img = Image.fromarray(gray, mode="L")
    gray_img.save(str(output_path))
    print(f"Gray image salva em: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python gray.py <input_color> <output_gray>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    to_grayscale(input_path, output_path)

# Art (scenes 1, 6, 11, 16)

Art wired at v1.1, repositioned at v1.2. These four files are crops of the uploaded
Light1 set, renamed for their scene. Replace a file in place to change the look; no
layout work needed.

| File | Source | Scene | Opacity |
|---|---|---|---|
| `scene01-hero.png` | 3Dtex-AI-Hero-01-Light1 | 1 Open | 0.62 (base) |
| `scene16-hero.png` | 3Dtex-AI-Hero-02-ToT_light1 | 16 Closer | 0.55 (inline) |
| `scene06-substrate.png` | 3Dtex-AI-BG-02-ToT_light1 | 6 Token path | 0.22 (inline) |
| `scene11-substrate.png` | 3Dtex-AI-BG-01-ToT_light1 | 11 Service horizon | 0.18 (inline) |

v1.2 moved the ridge from scene 13 to scene 11, where it is a horizon the service
beam crosses rather than a texture behind the dot wall. Scene 13 now stands on
white. The file was renamed with it; nothing else changed.

Rules that hold for anything dropped in here:

- Transparent or pure white ground, never black.
- 1920x1080 (16:9). `object-fit: cover` crops anything else.
- Upper 40 percent of the frame should stay empty: the type is center-aligned.
- No text, letters, numbers, logos, or people in the image.
- Red art only on scenes with no red interface element competing with it.
  That is why the two substrates use the ToT (red-free) treatment.

Scenes 1 and 16 no longer carry the dot field. The art replaces it; it does not
layer under it. Two textures in one plane compete.

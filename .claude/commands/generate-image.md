---
name: generate-image
description: Generate images using Gemini AI via gemini.py. Use when the user wants to create any AI-generated image.
---

Generate an image using the Gemini API.

1. Clarify what the user wants if the request is vague.
2. **If the image features a specific FM product:** Read the product's entry in `PRODUCT_VISUALS.md` for its visual description (colors, materials, shape). For extra accuracy, also view the reference photo from `images/Product Images/`. Include these details in your prompt so the generated image matches the real device.
3. Craft a detailed prompt based on the request, incorporating product visual details from step 2 if applicable.
4. **Only if the user asks for branded imagery:** Read BRANDING.md and incorporate FM's brand colors and style into the prompt. Do not apply branding by default.
5. Pick an aspect ratio that fits the use case (16:9 for banners, 1:1 for social, 9:16 for mobile, 4:3 for general).
6. Run: `python3 gemini.py image "<prompt>" --aspect <ratio>`
7. Tell the user the output path. Images save to `images/` by default.
8. To revise: `python3 gemini.py edit "<path>" "<instruction>"` or regenerate with a refined prompt.

If the user needs a full web page or component built around the image, hand off to the `/frontend-design` skill and reference BRANDING.md for colors and fonts there too.

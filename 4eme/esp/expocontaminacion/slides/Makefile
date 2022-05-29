html:
	mkdir -p _build
	hovercraft -sN contaminacion_slides.rst _build
	@echo firefox _build/index.html

hovercraft_tips:
	mkdir -p _build/tips
	hovercraft -sN hovercraft_tips.rst _build/tips
	@echo firefox _build/tips/index.html

zip_html:
	cp -fr _build contaminacion_mario_2022
	zip -r contaminacion_mario_2022.zip contaminacion_mario_2022
	@echo HTML slides are on contaminacion_mario_2022.zip

clean:
	rm -fr _build
	rm -fr contaminacion_mario_2022  contaminacion_mario_2022.zip

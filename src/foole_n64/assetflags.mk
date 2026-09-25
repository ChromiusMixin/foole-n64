#a list of custom asset flags to use when converting to Libradgon formats

filesystem/font/en/antipasto.font64: 			MKFONT_FLAGS+= --size 14  
filesystem/font/en/antipastomedium.font64: 		MKFONT_FLAGS+= --size 14  
filesystem/font/en/barlow.font64: 			MKFONT_FLAGS+= --size 14  
filesystem/font/en/nunito.font64: 			MKFONT_FLAGS+=  --size 18  
filesystem/font/en/nunitosemi.font64: 			MKFONT_FLAGS+= --size 16  
filesystem/font/en/SpecialElite.font64: 		MKFONT_FLAGS+= --size 18  

filesystem/bgm/mus_fantasia.wav64: 				AUDIOCONV_FLAGS += --wav-compress 1,bits=3 --wav-resample 24000
filesystem/bgm/mus_gallery.wav64: 				AUDIOCONV_FLAGS += --wav-compress 1,bits=3 --wav-resample 24000
filesystem/bgm/mus_infirmary.wav64: 				AUDIOCONV_FLAGS += --wav-compress 1,bits=3 --wav-resample 24000
filesystem/bgm/mus_vsfoole.wav64: 				AUDIOCONV_FLAGS += --wav-compress 1,bits=3 --wav-resample 24000
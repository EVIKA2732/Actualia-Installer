pkgname=actualia-installer
pkgver=1.0
pkgrel=1
pkgdesc="Install User Repository"
arch=('x86_64')
license=('MIT')
depends=('tk' 'python-pillow')
source=("main.py"
	"logo.png"
	"actualia.png"
	"actualia-installer.desktop")
sha512sums=('SKIP'
	    'SKIP'
	    'SKIP'
	    'SKIP')		
package() {
	install -Dm644 "actualia-installer.desktop" "${pkgdir}/usr/share/applications/actualia-installer.desktop"
        install -Dm644 "main.py" "${pkgdir}/usr/bin/actualia/main.py"
		install -Dm644 "logo.png" "${pkgdir}/usr/bin/actualia/logo.png"
        install -Dm644 "actualia.png" "${pkgdir}/usr/share/icons/actualia.png"
} 



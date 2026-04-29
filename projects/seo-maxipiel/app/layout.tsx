import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

const SITE_URL = "https://guia.maxipiel.com.mx";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "Guía de Piel para Tapiceros | Maxipiel",
    template: "%s | Maxipiel",
  },
  description:
    "Guías prácticas de piel y tapicería para profesionales. Aprende a elegir el cuero correcto para muebles, autos, calzado y marroquinería.",
  keywords: ["piel para tapicería", "cuero para muebles", "tapicería automotriz", "piel genuina México"],
  authors: [{ name: "Maxipiel" }],
  creator: "Maxipiel",
  publisher: "Maxipiel",
  openGraph: {
    type: "website",
    locale: "es_MX",
    url: SITE_URL,
    siteName: "Maxipiel — Guías de Piel y Tapicería",
    title: "Guía de Piel para Tapiceros | Maxipiel",
    description:
      "Guías prácticas de piel y tapicería para profesionales. Aprende a elegir el cuero correcto.",
  },
  twitter: {
    card: "summary_large_image",
    title: "Guía de Piel para Tapiceros | Maxipiel",
    description: "Guías prácticas de piel y tapicería para profesionales.",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: { index: true, follow: true },
  },
  alternates: {
    canonical: SITE_URL,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="es-MX" className={inter.variable}>
      <body className="min-h-screen bg-white text-gray-900 font-sans antialiased flex flex-col">
        <header className="border-b border-gray-100 py-4 px-6">
          <div className="max-w-4xl mx-auto flex items-center justify-between">
            <a href="/" className="text-xl font-bold text-red-800 hover:text-red-700">
              Maxipiel
            </a>
            <nav className="flex gap-6 text-sm text-gray-600">
              <a href="/guias/" className="hover:text-red-800">Guías</a>
              <a href="https://www.maxipiel.com.mx" target="_blank" rel="noopener" className="hover:text-red-800">
                Tienda
              </a>
            </nav>
          </div>
        </header>
        <main className="flex-1">{children}</main>
        <footer className="border-t border-gray-100 py-8 px-6 mt-16">
          <div className="max-w-4xl mx-auto text-center text-sm text-gray-500">
            <p>© {new Date().getFullYear()} Maxipiel — León, Guanajuato. Todos los derechos reservados.</p>
            <p className="mt-1">
              Visita nuestra{" "}
              <a href="https://www.maxipiel.com.mx" className="text-red-800 hover:underline" target="_blank" rel="noopener">
                tienda en línea
              </a>
            </p>
          </div>
        </footer>
      </body>
    </html>
  );
}

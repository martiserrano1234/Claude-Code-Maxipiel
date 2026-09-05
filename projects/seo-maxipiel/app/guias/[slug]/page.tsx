import { getAllPostSlugs, getPost } from "@/lib/posts";
import { notFound } from "next/navigation";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getAllPostSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPost(slug);
  if (!post) return {};

  const url = `https://guia.maxipiel.com.mx/guias/${slug}/`;

  return {
    title: post.title,
    description: post.description,
    keywords: post.keywords,
    openGraph: {
      title: post.title,
      description: post.description,
      url,
      type: "article",
      publishedTime: post.date,
      authors: ["Maxipiel"],
    },
    alternates: { canonical: url },
  };
}

/**
 * Saca las preguntas frecuentes del HTML del artículo.
 * Toma cada <h3> que aparece después del encabezado "Preguntas frecuentes"
 * y usa como respuesta el texto que le sigue hasta el próximo encabezado.
 * Si el artículo no tiene esa sección, devuelve lista vacía y no se emite
 * ningún FAQPage (marcar preguntas que no existen sería incorrecto).
 */
function extraerPreguntas(html: string): { pregunta: string; respuesta: string }[] {
  const inicio = html.search(/<h2[^>]*>\s*Preguntas frecuentes\s*<\/h2>/i);
  if (inicio === -1) return [];

  const seccion = html.slice(inicio);
  const limpiar = (s: string) =>
    s.replace(/<[^>]+>/g, " ").replace(/&amp;/g, "&").replace(/&quot;/g, '"')
      .replace(/&#39;/g, "'").replace(/\s+/g, " ").trim();

  const resultado: { pregunta: string; respuesta: string }[] = [];
  const bloques = [...seccion.matchAll(/<h3[^>]*>([\s\S]*?)<\/h3>([\s\S]*?)(?=<h3|<h2|$)/gi)];

  for (const b of bloques) {
    const pregunta = limpiar(b[1]);
    const respuesta = limpiar(b[2]);
    if (pregunta && respuesta.length > 20) {
      resultado.push({ pregunta, respuesta });
    }
  }
  return resultado;
}

export default async function ArticlePage({ params }: Props) {
  const { slug } = await params;
  const post = await getPost(slug);
  if (!post) notFound();

  // Extrae las preguntas frecuentes del artículo (los <h3> que siguen a la
  // sección "Preguntas frecuentes") para publicarlas como FAQPage. Los
  // buscadores y los modelos de IA leen ese formato directamente, en vez de
  // tener que inferir qué es pregunta y qué es respuesta dentro del texto.
  const faq = extraerPreguntas(post.content);

  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      ...(faq.length
        ? [
            {
              "@type": "FAQPage",
              mainEntity: faq.map((f) => ({
                "@type": "Question",
                name: f.pregunta,
                acceptedAnswer: { "@type": "Answer", text: f.respuesta },
              })),
            },
          ]
        : []),
      {
        "@type": "Article",
        headline: post.title,
        description: post.description,
        datePublished: post.date,
        author: { "@type": "Organization", name: "Maxipiel", url: "https://www.maxipiel.com.mx" },
        publisher: { "@type": "Organization", name: "Maxipiel", url: "https://www.maxipiel.com.mx" },
        mainEntityOfPage: { "@type": "WebPage", "@id": `https://guia.maxipiel.com.mx/guias/${slug}/` },
        keywords: post.keywords.join(", "),
        inLanguage: "es-MX",
      },
      {
        "@type": "BreadcrumbList",
        itemListElement: [
          { "@type": "ListItem", position: 1, name: "Inicio", item: "https://guia.maxipiel.com.mx/" },
          { "@type": "ListItem", position: 2, name: "Guías", item: "https://guia.maxipiel.com.mx/guias/" },
          { "@type": "ListItem", position: 3, name: post.title },
        ],
      },
    ],
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <article className="max-w-3xl mx-auto px-6 py-12">
        {/* Breadcrumb */}
        <nav className="text-sm text-gray-400 mb-8" aria-label="Breadcrumb">
          <a href="/" className="hover:text-red-800">Inicio</a>
          <span className="mx-2">/</span>
          <a href="/guias/" className="hover:text-red-800">Guías</a>
          <span className="mx-2">/</span>
          <span className="text-gray-600">{post.title}</span>
        </nav>

        {/* Header */}
        <header className="mb-10">
          <span className="text-xs text-red-700 font-medium uppercase tracking-wide">
            {post.category}
          </span>
          <h1 className="text-3xl font-extrabold text-gray-900 mt-2 mb-4 leading-tight">
            {post.title}
          </h1>
          <p className="text-lg text-gray-600 leading-relaxed">{post.description}</p>
          <div className="mt-4 flex items-center gap-4 text-sm text-gray-400">
            <span>{post.date}</span>
            <span>·</span>
            <span>{post.readingTime} de lectura</span>
          </div>
        </header>

        {/* Content */}
        <div
          className="prose prose-gray prose-lg max-w-none
            prose-headings:font-bold prose-headings:text-gray-900
            prose-h2:text-2xl prose-h2:mt-10 prose-h2:mb-4
            prose-h3:text-xl prose-h3:mt-8 prose-h3:mb-3
            prose-p:text-gray-700 prose-p:leading-relaxed
            prose-a:text-red-700 prose-a:no-underline hover:prose-a:underline
            prose-strong:text-gray-900
            prose-ul:text-gray-700 prose-ol:text-gray-700
            prose-table:text-sm
            prose-th:bg-red-800 prose-th:text-white prose-th:p-3
            prose-td:p-3 prose-td:border prose-td:border-gray-200"
          dangerouslySetInnerHTML={{ __html: post.content }}
        />

        {/* CTA */}
        <div className="mt-16 p-6 bg-red-50 border border-red-100 rounded-xl">
          <h3 className="font-bold text-gray-900 mb-2">¿Necesitas piel para tu proyecto?</h3>
          <p className="text-sm text-gray-600 mb-4">
            En Maxipiel tenemos piel genuina, cuero sintético y telas para tapicería. Envíos a todo México.
          </p>
          <a
            href="https://www.maxipiel.com.mx"
            target="_blank"
            rel="noopener"
            className="inline-block bg-red-800 text-white text-sm font-medium px-5 py-2.5 rounded-lg hover:bg-red-700 transition-colors"
          >
            Ver productos →
          </a>
        </div>
      </article>
    </>
  );
}

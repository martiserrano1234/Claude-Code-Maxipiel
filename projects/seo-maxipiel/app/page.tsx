import { getAllPosts } from "@/lib/posts";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Guía de Piel para Tapiceros | Maxipiel",
  description:
    "Todo lo que necesitas saber sobre piel y cuero para tapicería, muebles, calzado y marroquinería. Guías escritas por expertos de Maxipiel.",
};

export default function Home() {
  const posts = getAllPosts();
  const featured = posts.filter((p) => p.featured).slice(0, 3);
  const recent = posts.slice(0, 6);

  return (
    <div className="max-w-4xl mx-auto px-6 py-12">
      <section className="mb-16 text-center">
        <h1 className="text-4xl font-extrabold text-gray-900 mb-4 leading-tight">
          La guía definitiva de piel para tapiceros
        </h1>
        <p className="text-lg text-gray-600 max-w-2xl mx-auto">
          Artículos prácticos sobre tipos de cuero, técnicas de tapicería y cómo elegir el material
          correcto para cada proyecto. Directo desde León, Guanajuato.
        </p>
      </section>

      {featured.length > 0 && (
        <section className="mb-16">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Artículos destacados</h2>
          <div className="grid gap-6 md:grid-cols-3">
            {featured.map((post) => (
              <ArticleCard key={post.slug} post={post} />
            ))}
          </div>
        </section>
      )}

      {recent.length > 0 && (
        <section>
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Artículos recientes</h2>
          <div className="grid gap-6 md:grid-cols-2">
            {recent.map((post) => (
              <ArticleCard key={post.slug} post={post} />
            ))}
          </div>
        </section>
      )}

      {posts.length === 0 && (
        <section className="text-center py-20 text-gray-400">
          <p className="text-lg">Próximamente — los artículos están en camino.</p>
        </section>
      )}
    </div>
  );
}

function ArticleCard({ post }: { post: ReturnType<typeof getAllPosts>[0] }) {
  return (
    <a
      href={`/guias/${post.slug}/`}
      className="block border border-gray-100 rounded-xl p-5 hover:border-red-200 hover:shadow-sm transition-all group"
    >
      <span className="text-xs text-red-700 font-medium uppercase tracking-wide">
        {post.category}
      </span>
      <h3 className="text-base font-semibold text-gray-900 mt-2 mb-2 group-hover:text-red-800 leading-snug">
        {post.title}
      </h3>
      <p className="text-sm text-gray-500 line-clamp-2">{post.description}</p>
      <div className="mt-3 flex items-center gap-3 text-xs text-gray-400">
        <span>{post.date}</span>
        <span>·</span>
        <span>{post.readingTime} lectura</span>
      </div>
    </a>
  );
}

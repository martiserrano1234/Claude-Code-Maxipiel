import { getAllPosts } from "@/lib/posts";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Todas las Guías de Piel y Tapicería",
  description:
    "Biblioteca completa de guías sobre piel para tapiceros: tipos de cuero, técnicas, cuidado y mantenimiento. Aprende con Maxipiel.",
};

export default function GuiasIndex() {
  const posts = getAllPosts();

  const byCategory = posts.reduce<Record<string, typeof posts>>((acc, post) => {
    (acc[post.category] ??= []).push(post);
    return acc;
  }, {});

  return (
    <div className="max-w-4xl mx-auto px-6 py-12">
      <h1 className="text-3xl font-extrabold text-gray-900 mb-3">Guías de piel y tapicería</h1>
      <p className="text-gray-600 mb-12">
        {posts.length} artículos sobre tipos de cuero, técnicas y cómo elegir el material correcto.
      </p>

      {Object.entries(byCategory).map(([category, categoryPosts]) => (
        <section key={category} className="mb-12">
          <h2 className="text-xl font-bold text-gray-900 mb-4 pb-2 border-b border-gray-100">
            {category}
          </h2>
          <div className="space-y-4">
            {categoryPosts.map((post) => (
              <a
                key={post.slug}
                href={`/guias/${post.slug}/`}
                className="flex items-start justify-between gap-4 py-3 hover:text-red-800 group"
              >
                <div>
                  <h3 className="font-medium text-gray-900 group-hover:text-red-800">
                    {post.title}
                  </h3>
                  <p className="text-sm text-gray-500 mt-0.5">{post.description}</p>
                </div>
                <span className="text-xs text-gray-400 whitespace-nowrap mt-1">{post.readingTime}</span>
              </a>
            ))}
          </div>
        </section>
      ))}

      {posts.length === 0 && (
        <p className="text-gray-400 text-center py-20">Próximamente.</p>
      )}
    </div>
  );
}

import { getAllPosts } from "@/lib/posts";
import type { MetadataRoute } from "next";

export const dynamic = "force-static";

const BASE = "https://guia.maxipiel.com.mx";

export default function sitemap(): MetadataRoute.Sitemap {
  const posts = getAllPosts();

  const postEntries: MetadataRoute.Sitemap = posts.map((post) => ({
    url: `${BASE}/guias/${post.slug}/`,
    lastModified: new Date(post.date),
    changeFrequency: "monthly",
    priority: 0.8,
  }));

  return [
    { url: `${BASE}/`, lastModified: new Date(), changeFrequency: "weekly", priority: 1 },
    { url: `${BASE}/guias/`, lastModified: new Date(), changeFrequency: "weekly", priority: 0.9 },
    ...postEntries,
  ];
}
